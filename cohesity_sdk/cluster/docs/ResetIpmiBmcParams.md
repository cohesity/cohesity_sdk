# ResetIpmiBmcParams

Specifies the params to reset ipmi bmc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | Specifies the node id of the node for which ipmi bmc needs to be reset. This parameter is incompatible with &#39;nodeIp&#39;. | [optional] 
**node_ip** | **str** | Specifies the node id of the node for which ipmi bmc needs to be reset. This parameter is incompatible with &#39;nodeId&#39;. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.reset_ipmi_bmc_params import ResetIpmiBmcParams

# TODO update the JSON string below
json = "{}"
# create an instance of ResetIpmiBmcParams from a JSON string
reset_ipmi_bmc_params_instance = ResetIpmiBmcParams.from_json(json)
# print the JSON string representation of the object
print(ResetIpmiBmcParams.to_json())

# convert the object into a dict
reset_ipmi_bmc_params_dict = reset_ipmi_bmc_params_instance.to_dict()
# create an instance of ResetIpmiBmcParams from a dict
reset_ipmi_bmc_params_from_dict = ResetIpmiBmcParams.from_dict(reset_ipmi_bmc_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


