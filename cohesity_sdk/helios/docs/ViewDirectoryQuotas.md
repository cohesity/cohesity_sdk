# ViewDirectoryQuotas

Specifies a list of View directory quotas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookie** | **int** | Specifies the pagination cookie. | [optional] 
**directory_quotas** | [**List[ViewDirectoryQuota]**](ViewDirectoryQuota.md) | Specifies the list of View directory quotas. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.view_directory_quotas import ViewDirectoryQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of ViewDirectoryQuotas from a JSON string
view_directory_quotas_instance = ViewDirectoryQuotas.from_json(json)
# print the JSON string representation of the object
print(ViewDirectoryQuotas.to_json())

# convert the object into a dict
view_directory_quotas_dict = view_directory_quotas_instance.to_dict()
# create an instance of ViewDirectoryQuotas from a dict
view_directory_quotas_from_dict = ViewDirectoryQuotas.from_dict(view_directory_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


