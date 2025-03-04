# SitesDiscoveryParams

Specifies discovery params for SharePoint Site entities. It should only be populated if the 'DiscoveryParams.discoverableObjectTypeList' includes 'kSites' otherwise this will be ignored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_site_tagging** | **bool** | Specifies whether the SHarePoint Sites will be tagged whether they belong to a group site or teams site. | [optional] 

## Example

```python
from cohesity_sdk.models.sites_discovery_params import SitesDiscoveryParams

# TODO update the JSON string below
json = "{}"
# create an instance of SitesDiscoveryParams from a JSON string
sites_discovery_params_instance = SitesDiscoveryParams.from_json(json)
# print the JSON string representation of the object
print(SitesDiscoveryParams.to_json())

# convert the object into a dict
sites_discovery_params_dict = sites_discovery_params_instance.to_dict()
# create an instance of SitesDiscoveryParams from a dict
sites_discovery_params_from_dict = SitesDiscoveryParams.from_dict(sites_discovery_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


