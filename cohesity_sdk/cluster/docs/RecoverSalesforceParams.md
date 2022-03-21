# RecoverSalesforceParams

Specifies the recovery options specific to Salesforce environment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[CommonRecoverObjectSnapshotParams], none_type**](CommonRecoverObjectSnapshotParams.md) | Specifies the list of recover Object parameters. | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other salesforce objects if one of Object failed to recover. Default value is false. | [optional] 
**recover_to** | **int, none_type** | Specifies the id of registered source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**recover_sfdc_object_params** | [**RecoverSfdcObjectParams**](RecoverSfdcObjectParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


