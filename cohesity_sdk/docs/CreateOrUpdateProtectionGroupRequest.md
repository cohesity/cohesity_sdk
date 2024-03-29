# CreateOrUpdateProtectionGroupRequest

Specifies the request to create or update a Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the Protection Group. | 
**policy_id** | **str, none_type** | Specifies the unique id of the Protection Policy associated with the Protection Group. The Policy provides retry settings Protection Schedules, Priority, SLA, etc. | 
**environment** | **str, none_type** | Specifies the environment type of the Protection Group. | 
**priority** | **str, none_type** | Specifies the priority of the Protection Group. | [optional] 
**storage_domain_id** | **int, none_type** | Specifies the Storage Domain (View Box) ID where this Protection Group writes data. | [optional] 
**description** | **str, none_type** | Specifies a description of the Protection Group. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**end_time_usecs** | **int, none_type** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**alert_policy** | [**ProtectionGroupAlertingPolicy**](ProtectionGroupAlertingPolicy.md) |  | [optional] 
**sla** | [**[SlaRule], none_type**](SlaRule.md) | Specifies the SLA parameters for this Protection Group. | [optional] 
**qos_policy** | **str, none_type** | Specifies whether the Protection Group will be written to HDD or SSD. | [optional] 
**abort_in_blackouts** | **bool, none_type** | Specifies whether currently executing jobs should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if &#39;pauseInBlackouts&#39; is set to true. | [optional] 
**pause_in_blackouts** | **bool, none_type** | Specifies whether currently executing jobs should be paused if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if &#39;abortInBlackouts&#39; is sent as true. | [optional] 
**is_paused** | **bool, none_type** | Specifies if the the Protection Group is paused. New runs are not scheduled for the paused Protection Groups. Active run if any is not impacted. | [optional] 
**vmware_params** | [**VmwareProtectionGroupParams**](VmwareProtectionGroupParams.md) |  | [optional] 
**acropolis_params** | [**AcropolisProtectionGroupParams**](AcropolisProtectionGroupParams.md) |  | [optional] 
**kubernetes_params** | [**KubernetesProtectionGroupParams**](KubernetesProtectionGroupParams.md) |  | [optional] 
**mssql_params** | [**MSSQLProtectionGroupParams**](MSSQLProtectionGroupParams.md) |  | [optional] 
**oracle_params** | [**OracleProtectionGroupParams**](OracleProtectionGroupParams.md) |  | [optional] 
**view_params** | [**ViewProtectionGroupParams**](ViewProtectionGroupParams.md) |  | [optional] 
**pure_params** | [**PureProtectionGroupParams**](PureProtectionGroupParams.md) |  | [optional] 
**nimble_params** | [**NimbleProtectionGroupParams**](NimbleProtectionGroupParams.md) |  | [optional] 
**hyperv_params** | [**HyperVProtectionGroupParams**](HyperVProtectionGroupParams.md) |  | [optional] 
**aws_params** | [**AwsProtectionGroupParams**](AwsProtectionGroupParams.md) |  | [optional] 
**azure_params** | [**AzureProtectionGroupParams**](AzureProtectionGroupParams.md) |  | [optional] 
**gcp_params** | [**GcpProtectionGroupParams**](GcpProtectionGroupParams.md) |  | [optional] 
**kvm_params** | [**KvmProtectionGroupParams**](KvmProtectionGroupParams.md) |  | [optional] 
**physical_params** | [**PhysicalProtectionGroupParams**](PhysicalProtectionGroupParams.md) |  | [optional] 
**ad_params** | [**ADProtectionGroupParams**](ADProtectionGroupParams.md) |  | [optional] 
**office365_params** | [**Office365ProtectionGroupParams**](Office365ProtectionGroupParams.md) |  | [optional] 
**netapp_params** | [**NetappProtectionGroupParams**](NetappProtectionGroupParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasProtectionGroupParams**](GenericNasProtectionGroupParams.md) |  | [optional] 
**isilon_params** | [**IsilonProtectionGroupParams**](IsilonProtectionGroupParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeProtectionGroupParams**](FlashbladeProtectionGroupParams.md) |  | [optional] 
**gpfs_params** | [**GpfsProtectionGroupParams**](GpfsProtectionGroupParams.md) |  | [optional] 
**couchbase_params** | [**NoSqlProtectionGroupParams**](NoSqlProtectionGroupParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileProtectionGroupParams**](ElastifileProtectionGroupParams.md) |  | [optional] 
**cassandra_params** | [**CassandraProtectionGroupParams**](CassandraProtectionGroupParams.md) |  | [optional] 
**mongodb_params** | [**MongoDBProtectionGroupParams**](MongoDBProtectionGroupParams.md) |  | [optional] 
**hive_params** | [**NoSqlProtectionGroupParams**](NoSqlProtectionGroupParams.md) |  | [optional] 
**hdfs_params** | [**HdfsProtectionGroupParams**](HdfsProtectionGroupParams.md) |  | [optional] 
**hbase_params** | [**NoSqlProtectionGroupParams**](NoSqlProtectionGroupParams.md) |  | [optional] 
**remote_adapter_params** | [**RemoteAdapterProtectionGroupParams**](RemoteAdapterProtectionGroupParams.md) |  | [optional] 
**exchange_params** | [**ExchangeProtectionGroupParams**](ExchangeProtectionGroupParams.md) |  | [optional] 
**uda_params** | [**UdaProtectionGroupParams**](UdaProtectionGroupParams.md) |  | [optional] 
**sfdc_params** | [**SfdcProtectionGroupParams**](SfdcProtectionGroupParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


