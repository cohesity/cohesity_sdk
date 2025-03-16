# CommonPITRangesProtectedObjectResponse

Specifies common properties for PIT Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment for which restore ranges are returned. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_pit_ranges_protected_object_response import CommonPITRangesProtectedObjectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPITRangesProtectedObjectResponse from a JSON string
common_pit_ranges_protected_object_response_instance = CommonPITRangesProtectedObjectResponse.from_json(json)
# print the JSON string representation of the object
print(CommonPITRangesProtectedObjectResponse.to_json())

# convert the object into a dict
common_pit_ranges_protected_object_response_dict = common_pit_ranges_protected_object_response_instance.to_dict()
# create an instance of CommonPITRangesProtectedObjectResponse from a dict
common_pit_ranges_protected_object_response_from_dict = CommonPITRangesProtectedObjectResponse.from_dict(common_pit_ranges_protected_object_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


