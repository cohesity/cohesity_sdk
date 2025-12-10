# GoogleWorkspaceSourceRegistrationParams

Specifies the paramaters to register a Google Workspace source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_user_email** | **str** | Specifies the Admin&#39;s User Email for authentication. | 
**service_account_json** | **str** | Specifies the Service Account JSON credentials. | 
**use_cases** | **List[str]** | The use cases for which the source is to be registered. | 

## Example

```python
from cohesity_sdk.cluster.models.google_workspace_source_registration_params import GoogleWorkspaceSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceSourceRegistrationParams from a JSON string
google_workspace_source_registration_params_instance = GoogleWorkspaceSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceSourceRegistrationParams.to_json())

# convert the object into a dict
google_workspace_source_registration_params_dict = google_workspace_source_registration_params_instance.to_dict()
# create an instance of GoogleWorkspaceSourceRegistrationParams from a dict
google_workspace_source_registration_params_from_dict = GoogleWorkspaceSourceRegistrationParams.from_dict(google_workspace_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


