# RecoverServiceNowParams

Specifies the recovery params specific to ServiceNow recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other ServiceNow tables if one of tables failed to recover. Default value is false. | [optional] 
**error_count** | **int** | Specifies the number of errors we faced while trying to restore ServiceNow tables. | [optional] 
**instance** | [**RecoverServiceNowInstanceParams**](RecoverServiceNowInstanceParams.md) |  | [optional] 
**recover_to** | **int** | Specifies the id of registered source where the tables are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**tables** | [**List[RecoverServiceNowTableParams]**](RecoverServiceNowTableParams.md) | Specifies the params for table level recovery. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_service_now_params import RecoverServiceNowParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverServiceNowParams from a JSON string
recover_service_now_params_instance = RecoverServiceNowParams.from_json(json)
# print the JSON string representation of the object
print(RecoverServiceNowParams.to_json())

# convert the object into a dict
recover_service_now_params_dict = recover_service_now_params_instance.to_dict()
# create an instance of RecoverServiceNowParams from a dict
recover_service_now_params_from_dict = RecoverServiceNowParams.from_dict(recover_service_now_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


