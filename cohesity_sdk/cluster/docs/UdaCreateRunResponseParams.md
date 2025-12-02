# UdaCreateRunResponseParams

Specifies the response for creation of a Universal Data Adapter protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externally_triggered_run_id** | **str** | Specifies a unique run id for an externally triggered run. This id can be used by the caller to identify the corresponding backup process on the source host. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.uda_create_run_response_params import UdaCreateRunResponseParams

# TODO update the JSON string below
json = "{}"
# create an instance of UdaCreateRunResponseParams from a JSON string
uda_create_run_response_params_instance = UdaCreateRunResponseParams.from_json(json)
# print the JSON string representation of the object
print(UdaCreateRunResponseParams.to_json())

# convert the object into a dict
uda_create_run_response_params_dict = uda_create_run_response_params_instance.to_dict()
# create an instance of UdaCreateRunResponseParams from a dict
uda_create_run_response_params_from_dict = UdaCreateRunResponseParams.from_dict(uda_create_run_response_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


