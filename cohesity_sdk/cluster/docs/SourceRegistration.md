# SourceRegistration

Specifies the Source Registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a protection source. | [optional] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. This field will be depricated in future. Use connections field. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specfies the list of connections for the source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | [optional] 
**id** | **int** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**name** | **str** | The user specified name for this source. | [optional] 
**source_id** | **int** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**source_info** | [**Object**](Object.md) |  | [optional] 
**authentication_status** | **str** | Specifies the status of the authentication during the registration of a Protection Source. &#39;Pending&#39; indicates the authentication is in progress. &#39;Scheduled&#39; indicates the authentication is scheduled. &#39;Finished&#39; indicates the authentication is completed. &#39;RefreshInProgress&#39; indicates the refresh is in progress. | [optional] [readonly] 
**last_refreshed_time_msecs** | **int** | Specifies the time when the source was last refreshed in milliseconds. | [optional] [readonly] 
**registration_time_msecs** | **int** | Specifies the time when the source was registered in milliseconds | [optional] [readonly] 
**aws_params** | [**AwsSourceRegistrationParams**](AwsSourceRegistrationParams.md) |  | [optional] 
**azure_params** | [**AzureSourceRegistrationParams**](AzureSourceRegistrationParams.md) |  | [optional] 
**cassandra_params** | [**CassandraSourceRegistrationParams**](CassandraSourceRegistrationParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseSourceRegistrationParams**](CouchbaseSourceRegistrationParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileRegistrationParams**](ElastifileRegistrationParams.md) |  | [optional] 
**external_metadata** | [**EntityExternalMetadata**](EntityExternalMetadata.md) |  | [optional] 
**flashblade_params** | [**FlashbladeRegistrationParams**](FlashbladeRegistrationParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasRegistrationParams**](GenericNasRegistrationParams.md) |  | [optional] 
**gpfs_params** | [**GpfsRegistrationParams**](GpfsRegistrationParams.md) |  | [optional] 
**hbase_params** | [**HbaseSourceRegistrationParams**](HbaseSourceRegistrationParams.md) |  | [optional] 
**hdfs_params** | [**HdfsSourceRegistrationParams**](HdfsSourceRegistrationParams.md) |  | [optional] 
**hive_params** | [**HiveSourceRegistrationParams**](HiveSourceRegistrationParams.md) |  | [optional] 
**hyperv_params** | [**HyperVSourceRegistrationParams**](HyperVSourceRegistrationParams.md) |  | [optional] 
**isilon_params** | [**IsilonRegistrationParams**](IsilonRegistrationParams.md) |  | [optional] 
**mongodb_params** | [**MongoDBSourceRegistrationParams**](MongoDBSourceRegistrationParams.md) |  | [optional] 
**netapp_params** | [**NetappRegistrationParams**](NetappRegistrationParams.md) |  | [optional] 
**office365_params** | [**Office365SourceRegistrationParams**](Office365SourceRegistrationParams.md) |  | [optional] 
**physical_params** | [**PhysicalSourceRegistrationParams**](PhysicalSourceRegistrationParams.md) |  | [optional] 
**sfdc_params** | [**SfdcSourceRegistrationParams**](SfdcSourceRegistrationParams.md) |  | [optional] 
**uda_params** | [**UdaSourceRegistrationParams**](UdaSourceRegistrationParams.md) |  | [optional] 
**vmware_params** | [**VmwareSourceRegistrationParams**](VmwareSourceRegistrationParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.source_registration import SourceRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of SourceRegistration from a JSON string
source_registration_instance = SourceRegistration.from_json(json)
# print the JSON string representation of the object
print(SourceRegistration.to_json())

# convert the object into a dict
source_registration_dict = source_registration_instance.to_dict()
# create an instance of SourceRegistration from a dict
source_registration_from_dict = SourceRegistration.from_dict(source_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


