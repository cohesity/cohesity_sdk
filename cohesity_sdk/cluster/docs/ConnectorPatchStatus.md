# ConnectorPatchStatus

Specifies patch status for the data-source connector. For example when the patch started, current status of the patch, errors for patch failure etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Specifies error message for patch failure. Will be non empty if the patch failed. In all other cases, this will be empty. | [optional] 
**last_status_fetched_timestamp_msecs** | **int** | Specifies the most recent timestamp in UNIX time (milliseconds) when the connector patch status(InProgress/ Failed/Success/NotStarted) was fetched. | [optional] 
**start_timestamp_msecs** | **int** | Specifies the timestamp in UNIX time (milliseconds) when the connector patch was triggered. | [optional] 
**status** | **str** | Specifies the last fetched patch status of the connector. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.connector_patch_status import ConnectorPatchStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorPatchStatus from a JSON string
connector_patch_status_instance = ConnectorPatchStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectorPatchStatus.to_json())

# convert the object into a dict
connector_patch_status_dict = connector_patch_status_instance.to_dict()
# create an instance of ConnectorPatchStatus from a dict
connector_patch_status_from_dict = ConnectorPatchStatus.from_dict(connector_patch_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


