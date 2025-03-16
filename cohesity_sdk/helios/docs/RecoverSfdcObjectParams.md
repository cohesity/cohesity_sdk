# RecoverSfdcObjectParams

Specifies the parameters to recover Salesforce objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_object_ids** | **List[str]** | Specifies a list of child object IDs to include in the recovery. Specified object IDs will also be recovered as part of this recovery. | [optional] 
**filter_query** | **str** | Specifies a Query to filter the records. This filtered list of records will be used for recovery. | [optional] 
**include_deleted_objects** | **bool** | Specifies whether to include deleted Objects in the recovery. | 
**mutation_types** | **List[str]** | Specifies a list of mutuation types for an object. Mutation type is required in conjunction with &#39;filterQuery&#39;. | [optional] 
**object_name** | **str** | Specifies the name of the object to be restored. | [optional] 
**parent_object_ids** | **List[str]** | Specifies a list of parent object IDs to include in recovery. Specified parent objects will also be recovered as part of this recovery. | [optional] 
**records** | **List[str]** | Specifies a list of records IDs to be recovered for the specified Object. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_sfdc_object_params import RecoverSfdcObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverSfdcObjectParams from a JSON string
recover_sfdc_object_params_instance = RecoverSfdcObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverSfdcObjectParams.to_json())

# convert the object into a dict
recover_sfdc_object_params_dict = recover_sfdc_object_params_instance.to_dict()
# create an instance of RecoverSfdcObjectParams from a dict
recover_sfdc_object_params_from_dict = RecoverSfdcObjectParams.from_dict(recover_sfdc_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


