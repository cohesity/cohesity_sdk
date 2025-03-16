# McmSourceRegistration

Specifies a Protection Source registration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id. | [optional] [readonly] 
**cluster_incarnation_id** | **int** | Specifies the cluster incarnation id. | [optional] [readonly] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specifies the list of connections associated with this source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | [optional] 
**id** | **str** | Source Registration ID. This can be used to retrieve, edit or delete the source registration. | [optional] [readonly] 
**name** | **str** | The user specified name for this source. | [optional] [readonly] 
**region_id** | **str** | Specifies the region id. | [optional] [readonly] 
**source_id** | **str** | ID of top level source object discovered after the registration. | [optional] [readonly] 
**aws_params** | [**AwsSourceRegistrationParams**](AwsSourceRegistrationParams.md) |  | [optional] 
**azure_params** | [**AzureSourceRegistrationParams**](AzureSourceRegistrationParams.md) |  | [optional] 
**cassandra_params** | [**CassandraSourceRegistrationParams**](CassandraSourceRegistrationParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseSourceRegistrationParams**](CouchbaseSourceRegistrationParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasRegistrationParams**](GenericNasRegistrationParams.md) |  | [optional] 
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
from cohesity_sdk.helios.models.mcm_source_registration import McmSourceRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of McmSourceRegistration from a JSON string
mcm_source_registration_instance = McmSourceRegistration.from_json(json)
# print the JSON string representation of the object
print(McmSourceRegistration.to_json())

# convert the object into a dict
mcm_source_registration_dict = mcm_source_registration_instance.to_dict()
# create an instance of McmSourceRegistration from a dict
mcm_source_registration_from_dict = McmSourceRegistration.from_dict(mcm_source_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


