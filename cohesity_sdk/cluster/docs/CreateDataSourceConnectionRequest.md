# CreateDataSourceConnectionRequest

Specifies parameters, like connection name, for the request to create a data-source connection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_vips** | **List[str]** | List of cluster virtual IPs associated with the connection. | [optional] 
**connection_name** | **str** | Specifies the name of the connection being created. For a given tenant, different connections can&#39;t have the same name. However, two (or more) different tenants can each have a connection with the same name. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.create_data_source_connection_request import CreateDataSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDataSourceConnectionRequest from a JSON string
create_data_source_connection_request_instance = CreateDataSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDataSourceConnectionRequest.to_json())

# convert the object into a dict
create_data_source_connection_request_dict = create_data_source_connection_request_instance.to_dict()
# create an instance of CreateDataSourceConnectionRequest from a dict
create_data_source_connection_request_from_dict = CreateDataSourceConnectionRequest.from_dict(create_data_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


