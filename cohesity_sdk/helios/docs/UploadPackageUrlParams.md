# UploadPackageUrlParams

Parameters to upload a package to the cluster by URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL where the package is hosted. | 

## Example

```python
from cohesity_sdk.helios.models.upload_package_url_params import UploadPackageUrlParams

# TODO update the JSON string below
json = "{}"
# create an instance of UploadPackageUrlParams from a JSON string
upload_package_url_params_instance = UploadPackageUrlParams.from_json(json)
# print the JSON string representation of the object
print(UploadPackageUrlParams.to_json())

# convert the object into a dict
upload_package_url_params_dict = upload_package_url_params_instance.to_dict()
# create an instance of UploadPackageUrlParams from a dict
upload_package_url_params_from_dict = UploadPackageUrlParams.from_dict(upload_package_url_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


