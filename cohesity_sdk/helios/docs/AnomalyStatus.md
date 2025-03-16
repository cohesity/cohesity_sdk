# AnomalyStatus

Details of the anomaly status of this run for this object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_strength** | **int** | The strenght of the anomaly between 1 and 100 | [optional] 
**is_anomaly** | **bool** | Indicates whether this protection run is anomalous | [optional] 

## Example

```python
from cohesity_sdk.helios.models.anomaly_status import AnomalyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyStatus from a JSON string
anomaly_status_instance = AnomalyStatus.from_json(json)
# print the JSON string representation of the object
print(AnomalyStatus.to_json())

# convert the object into a dict
anomaly_status_dict = anomaly_status_instance.to_dict()
# create an instance of AnomalyStatus from a dict
anomaly_status_from_dict = AnomalyStatus.from_dict(anomaly_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


