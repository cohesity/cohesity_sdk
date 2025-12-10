# ArtifactUrl

Specifies the URL of an artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_headers** | [**List[AuthHeader]**](AuthHeader.md) | HTTP headers to be included in download requests for the purposes of authenticating the client, in case the package is hosted in secure file server or artifactory.  | [optional] 
**url** | **str** | The URL where the artifact can be downloaded from.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.artifact_url import ArtifactUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactUrl from a JSON string
artifact_url_instance = ArtifactUrl.from_json(json)
# print the JSON string representation of the object
print(ArtifactUrl.to_json())

# convert the object into a dict
artifact_url_dict = artifact_url_instance.to_dict()
# create an instance of ArtifactUrl from a dict
artifact_url_from_dict = ArtifactUrl.from_dict(artifact_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


