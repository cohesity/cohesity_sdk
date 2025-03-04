# TeamsAdditionalParams

Specifies additional params for Teams entities. It should only be populated if the 'DiscoveryParams.discoverableObjectTypeList' includes 'kTeams' otherwise this will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_posts_backup** | **bool** | Specifies whether the Teams posts/conversations will be backed up or not. If this is false or not specified teams&#39; posts backup will not be done. | [optional] 

## Example

```python
from cohesity_sdk.models.teams_additional_params import TeamsAdditionalParams

# TODO update the JSON string below
json = "{}"
# create an instance of TeamsAdditionalParams from a JSON string
teams_additional_params_instance = TeamsAdditionalParams.from_json(json)
# print the JSON string representation of the object
print(TeamsAdditionalParams.to_json())

# convert the object into a dict
teams_additional_params_dict = teams_additional_params_instance.to_dict()
# create an instance of TeamsAdditionalParams from a dict
teams_additional_params_from_dict = TeamsAdditionalParams.from_dict(teams_additional_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


