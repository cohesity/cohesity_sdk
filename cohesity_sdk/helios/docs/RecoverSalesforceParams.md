# RecoverSalesforceParams

Specifies the recovery options specific to Salesforce environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other salesforce objects if one of Object failed to recover. Default value is false. | [optional] 
**objects** | [**List[CommonRecoverObjectSnapshotParams]**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recover_sfdc_object_params** | [**RecoverSfdcObjectParams**](RecoverSfdcObjectParams.md) |  | [optional] 
**recover_to** | **int** | Specifies the id of registered source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.helios.models.recover_salesforce_params import RecoverSalesforceParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverSalesforceParams from a JSON string
recover_salesforce_params_instance = RecoverSalesforceParams.from_json(json)
# print the JSON string representation of the object
print(RecoverSalesforceParams.to_json())

# convert the object into a dict
recover_salesforce_params_dict = recover_salesforce_params_instance.to_dict()
# create an instance of RecoverSalesforceParams from a dict
recover_salesforce_params_from_dict = RecoverSalesforceParams.from_dict(recover_salesforce_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


