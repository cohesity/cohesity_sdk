# SwiftConfig

Specifies the Swift config settings for this View.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swift_project_domain** | **str** | Specifies the Keystone project domain. | [optional] 
**swift_project_name** | **str** | Specifies the Keystone project name. | [optional] 
**swift_user_domain** | **str** | Specifies the Keystone user domain. | [optional] 
**swift_username** | **str** | Specifies the Keystone username. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.swift_config import SwiftConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SwiftConfig from a JSON string
swift_config_instance = SwiftConfig.from_json(json)
# print the JSON string representation of the object
print(SwiftConfig.to_json())

# convert the object into a dict
swift_config_dict = swift_config_instance.to_dict()
# create an instance of SwiftConfig from a dict
swift_config_from_dict = SwiftConfig.from_dict(swift_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


