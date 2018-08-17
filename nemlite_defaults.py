import filters as fl

names = {'DISPATCHLOAD': 'PUBLIC_DVD_DISPATCHLOAD',
         'DUDETAILSUMMARY': 'PUBLIC_DVD_DUDETAILSUMMARY',
         'DISPATCHCONSTRAINT': 'PUBLIC_DVD_DISPATCHCONSTRAINT',
         'GENCONDATA': 'PUBLIC_DVD_GENCONDATA',
         'DISPATCH_UNIT_SCADA': 'PUBLIC_DVD_DISPATCH_UNIT_SCADA',
         'DISPATCHPRICE': 'PUBLIC_DVD_DISPATCHPRICE',
         'SPDREGIONCONSTRAINT': 'PUBLIC_DVD_SPDREGIONCONSTRAINT',
         'SPDCONNECTIONPOINTCONSTRAINT': 'PUBLIC_DVD_SPDCONNECTIONPOINTCONSTRAINT',
         'SPDINTERCONNECTORCONSTRAINT': 'PUBLIC_DVD_SPDINTERCONNECTORCONSTRAINT',
         'BIDPEROFFER_D': 'PUBLIC_DVD_BIDPEROFFER_D',
         'DISPATCHINTERCONNECTORRES': 'PUBLIC_DVD_DISPATCHINTERCONNECTORRES',
         'BIDDAYOFFER_D': 'PUBLIC_DVD_BIDDAYOFFER_D',
         'DISPATCHREGIONSUM': 'PUBLIC_DVD_DISPATCHREGIONSUM',
         'FCAS_4_SECOND': 'FCAS',
         'ELEMENTS_FCAS_4_SECOND': 'Elements_FCAS.csv',
         'VARIABLES_FCAS_4_SECOND': '820-0079 csv.csv',
         'MASTER_REGISTRATION_LIST': 'NEM Registration and Exemption List'}

parent_tables = ['DUDETAILSUMMARY', 'INTERCONNECTORCONSTRAINT', 'INTERCONNECTOR', 'LOSSMODEL', 'MNSP_INTERCONNECTOR',
                 'MNSP_PEROFFER', 'DISPATCHCONSTRAINT', 'BIDPEROFFER_D', 'DISPATCHLOAD', 'GENCONDATA',
                 'SPDCONNECTIONPOINTCONSTRAINT', 'SPDINTERCONNECTORCONSTRAINT', 'DISPATCHINTERCONNECTORRES',
                 'DISPATCHPRICE', 'SPDREGIONCONSTRAINT', 'BIDDAYOFFER_D', 'MNSP_DAYOFFER', 'LOSSFACTORMODEL',
                 'DISPATCHREGIONSUM']

child_parent_map = {'connection_point_constraints': ['SPDCONNECTIONPOINTCONSTRAINT'],
                    'constraint_data': ['GENCONDATA', 'DISPATCHCONSTRAINT'],
                    'interconnector_constraints': ['SPDINTERCONNECTORCONSTRAINT'],
                    'capacity_bids': ['BIDPEROFFER_D'], # Dispatch load should get merged here.
                    'interconnectors': ['INTERCONNECTOR', 'INTERCONNECTORCONSTRAINT'],
                    'market_interconnectors': ['MNSP_INTERCONNECTOR'],
                    'generator_information': ['DUDETAILSUMMARY'],
                    'region_constraints': ['SPDREGIONCONSTRAINT'],
                    'price_bids': ['BIDDAYOFFER_D'],
                    'market_interconnector_price_bids': ['MNSP_DAYOFFER'],
                    'market_interconnector_capacity_bids': ['MNSP_PEROFFER'],
                    'initial_conditions': ['DISPATCHLOAD'],
                    'interconnector_segments': ['LOSSMODEL', 'DISPATCHINTERCONNECTORRES'],
                    'interconnector_dynamic_loss_coefficients': ['LOSSFACTORMODEL'],
                    'demand': ['DISPATCHREGIONSUM']}

parent_merge_cols = {'connection_point_constraints': None,
                     'constraint_data': ['GENCONID', 'EFFECTIVEDATE', 'VERSIONNO'],
                     'interconnector_constraints': None,
                     'capacity_bids': ['DUID'],
                     'interconnectors': ['INTERCONNECTORID'],
                     'market_interconnectors': None,
                     'generator_information': None,
                     'region_constraints': None,
                     'price_bids': None,
                     'market_interconnector_price_bids': None,
                     'market_interconnector_capacity_bids': None,
                     'initial_conditions': None,
                     'interconnector_segments': ['INTERCONNECTORID'],
                     'interconnector_dynamic_loss_coefficients': None,
                     'demand': None}

required_cols = {'SPDCONNECTIONPOINTCONSTRAINT': None,
                 'GENCONDATA': None,
                 'SPDINTERCONNECTORCONSTRAINT': None,
                 'BIDPEROFFER_D': None,
                 'DISPATCHINTERCONNECTORRES': ('INTERCONNECTORID', 'DISPATCHINTERVAL'),
                 'INTERCONNECTOR': ('INTERCONNECTORID', 'REGIONFROM', 'REGIONTO'),
                 'INTERCONNECTORCONSTRAINT': ('INTERCONNECTORID', 'MAXMWIN', 'MAXMWOUT', 'LOSSCONSTANT',
                                              'LOSSFLOWCOEFFICIENT', 'FROMREGIONLOSSSHARE', 'ICTYPE'),
                 'MNSP_INTERCONNECTOR': ('INTERCONNECTORID', 'LINKID', 'FROMREGION', 'TOREGION', 'MAXCAPACITY',
                                         'FROM_REGION_TLF', 'TO_REGION_TLF', 'LHSFACTOR'),
                 'DISPATCHPRICE': None,
                 'DUDETAILSUMMARY': ('DUID', 'END_DATE', 'DISPATCHTYPE', 'CONNECTIONPOINTID', 'REGIONID', 'LASTCHANGED',
                                     'TRANSMISSIONLOSSFACTOR', 'DISTRIBUTIONLOSSFACTOR'),
                 'DISPATCHCONSTRAINT': ('GENCONID', 'RHS', 'VERSIONNO', 'EFFECTIVEDATE'),
                 'SPDREGIONCONSTRAINT': None,
                 'BIDDAYOFFER_D': None,
                 'MNSP_DAYOFFER': ('LINKID', 'PRICEBAND1', 'PRICEBAND2', 'PRICEBAND3', 'PRICEBAND4', 'PRICEBAND5',
                                   'PRICEBAND6', 'PRICEBAND7', 'PRICEBAND8', 'PRICEBAND9', 'PRICEBAND10'),
                 'MNSP_PEROFFER': ('LINKID', 'BANDAVAIL1', 'BANDAVAIL2', 'BANDAVAIL3', 'BANDAVAIL4', 'BANDAVAIL5',
                                   'BANDAVAIL6', 'BANDAVAIL7', 'BANDAVAIL8', 'BANDAVAIL9', 'BANDAVAIL10', 'MAXAVAIL',
                                   'RAMPUPRATE'),
                 'DISPATCHLOAD': None,
                 'LOSSMODEL': None,
                 'LOSSFACTORMODEL': None,
                 'DISPATCHREGIONSUM': None}

wrapper_map = {'SPDCONNECTIONPOINTCONSTRAINT': None,
               'GENCONDATA': None,
               'SPDINTERCONNECTORCONSTRAINT': None,
               'BIDPEROFFER_D': fl.filter_on_interval_datetime,
               'DISPATCHINTERCONNECTORRES': fl.filter_on_settlementdate,
               'INTERCONNECTOR': fl.filter_on_last_changed,
               'INTERCONNECTORCONSTRAINT': fl.filter_on_effective_date,
               'MNSP_INTERCONNECTOR': fl.filter_on_effective_date,
               'DISPATCHPRICE': fl.filter_on_settlementdate,
               'DUDETAILSUMMARY': fl.filter_on_start_and_end_date,
               'DISPATCHCONSTRAINT': fl.filter_on_settlementdate,
               'SPDREGIONCONSTRAINT': None,
               'BIDDAYOFFER_D': fl.filter_on_settlementdate,
               'MNSP_DAYOFFER': fl.filter_on_settlementdate,
               'MNSP_PEROFFER': fl.filter_on_date_and_peroid,
               'DISPATCHLOAD': fl.filter_on_settlementdate,
               'LOSSMODEL': fl.filter_on_effective_date,
               'LOSSFACTORMODEL': fl.filter_on_effective_date,
               'DISPATCHREGIONSUM': fl.filter_on_settlementdate}

aemo_data_suffix = 'PUBLIC_DVD_'
