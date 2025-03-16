# QosPoliciesResult

Specifies the list of QoS policies.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qos_policies** | [**List[QoS]**](QoS.md) | Specifies the list of QoS policies. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.qos_policies_result import QosPoliciesResult

# TODO update the JSON string below
json = "{}"
# create an instance of QosPoliciesResult from a JSON string
qos_policies_result_instance = QosPoliciesResult.from_json(json)
# print the JSON string representation of the object
print(QosPoliciesResult.to_json())

# convert the object into a dict
qos_policies_result_dict = qos_policies_result_instance.to_dict()
# create an instance of QosPoliciesResult from a dict
qos_policies_result_from_dict = QosPoliciesResult.from_dict(qos_policies_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


