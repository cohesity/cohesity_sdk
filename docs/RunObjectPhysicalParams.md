# RunObjectPhysicalParams

Specifies physical parameters for this run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_file_path** | **str** | Specifies metadata file path during run-now requests for physical file based backups for some specific source. If specified, it will override any default metadata/directive file path set at the object level for the source. Also note that if the job default does not specify a metadata/directive file path for the source, then specifying this field for that source during run-now request will be rejected. | [optional] 

## Example

```python
from cohesity_sdk.models.run_object_physical_params import RunObjectPhysicalParams

# TODO update the JSON string below
json = "{}"
# create an instance of RunObjectPhysicalParams from a JSON string
run_object_physical_params_instance = RunObjectPhysicalParams.from_json(json)
# print the JSON string representation of the object
print(RunObjectPhysicalParams.to_json())

# convert the object into a dict
run_object_physical_params_dict = run_object_physical_params_instance.to_dict()
# create an instance of RunObjectPhysicalParams from a dict
run_object_physical_params_from_dict = RunObjectPhysicalParams.from_dict(run_object_physical_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


