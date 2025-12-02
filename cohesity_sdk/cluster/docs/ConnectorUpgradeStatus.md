# ConnectorUpgradeStatus

Specifies upgrade status for the data-source connector. For example when the upgrade started, current status of the upgrade, errors for upgrade failure etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_status_fetched_timestamp_msecs** | **int** | Specifies the last timestamp in UNIX time (milliseconds) when the connector upgrade status was fetched. | [optional] 
**message** | **str** | Specifies error message for upgrade failure. | [optional] 
**start_timestamp_m_secs** | **int** | Specifies the last timestamp in UNIX time (milliseconds) when the connector upgrade was triggered. | [optional] 
**status** | **str** | Specifies the last fetched upgrade status of the connector. | 

## Example

```python
from cohesity_sdk.cluster.models.connector_upgrade_status import ConnectorUpgradeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorUpgradeStatus from a JSON string
connector_upgrade_status_instance = ConnectorUpgradeStatus.from_json(json)
# print the JSON string representation of the object
print(ConnectorUpgradeStatus.to_json())

# convert the object into a dict
connector_upgrade_status_dict = connector_upgrade_status_instance.to_dict()
# create an instance of ConnectorUpgradeStatus from a dict
connector_upgrade_status_from_dict = ConnectorUpgradeStatus.from_dict(connector_upgrade_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


