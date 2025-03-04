# Office365PreservationHoldLibraryParams

Specifies the parameters specific to the protection of the Preservation Hold library. The Preservation Hold library is a hidden system location that isn't designed to be used interactively but instead, automatically stores files when this is needed for compliance reasons. It's not supported to edit, delete, or move these automatically retained files yourself. Instead, use compliance tools, such as those supported by eDiscovery to access these files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_protect** | **bool** | Specifies whether to protect the preservation hold library drive if one exists. Default is false. | [optional] 

## Example

```python
from cohesity_sdk.models.office365_preservation_hold_library_params import Office365PreservationHoldLibraryParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365PreservationHoldLibraryParams from a JSON string
office365_preservation_hold_library_params_instance = Office365PreservationHoldLibraryParams.from_json(json)
# print the JSON string representation of the object
print(Office365PreservationHoldLibraryParams.to_json())

# convert the object into a dict
office365_preservation_hold_library_params_dict = office365_preservation_hold_library_params_instance.to_dict()
# create an instance of Office365PreservationHoldLibraryParams from a dict
office365_preservation_hold_library_params_from_dict = Office365PreservationHoldLibraryParams.from_dict(office365_preservation_hold_library_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


