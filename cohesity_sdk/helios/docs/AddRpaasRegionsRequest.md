# AddRpaasRegionsRequest

Request params for enabling rpaas regions for the logged in account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[AddRegionParams]**](AddRegionParams.md) | List of regions being added. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.add_rpaas_regions_request import AddRpaasRegionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddRpaasRegionsRequest from a JSON string
add_rpaas_regions_request_instance = AddRpaasRegionsRequest.from_json(json)
# print the JSON string representation of the object
print(AddRpaasRegionsRequest.to_json())

# convert the object into a dict
add_rpaas_regions_request_dict = add_rpaas_regions_request_instance.to_dict()
# create an instance of AddRpaasRegionsRequest from a dict
add_rpaas_regions_request_from_dict = AddRpaasRegionsRequest.from_dict(add_rpaas_regions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


