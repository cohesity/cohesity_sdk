# AwsCloudC2SParams

Specifies the parameters which are specific to AWS related External Targets with Cloud Type C2S.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agency** | **str** | Specifies agency of the External Target. | 
**base_url** | **str** | Specifies base url of the External Target. | 
**c2s_type** | **str** | Specifies C2S type of the External Target C2S or SC2S. C2S is for Top secrect Cloud Services. In case the type is not provided, default value is assumed as C2S. | [optional] 
**client_certificate** | **str** | Specifies client certificate of the External Target | [optional] 
**client_certificate_password** | **str** | Specifies client certificate password of the External Target | [optional] 
**client_private_key** | **str** | Specifies client private key of the External Target | [optional] 
**mission** | **str** | Specifies mission of the External Target | 
**role** | **str** | Specifies role of the External Target | 
**server_ca_trusted_certificate** | **str** | Specifies server CA trusted certificate of the External Target | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_cloud_c2_s_params import AwsCloudC2SParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCloudC2SParams from a JSON string
aws_cloud_c2_s_params_instance = AwsCloudC2SParams.from_json(json)
# print the JSON string representation of the object
print(AwsCloudC2SParams.to_json())

# convert the object into a dict
aws_cloud_c2_s_params_dict = aws_cloud_c2_s_params_instance.to_dict()
# create an instance of AwsCloudC2SParams from a dict
aws_cloud_c2_s_params_from_dict = AwsCloudC2SParams.from_dict(aws_cloud_c2_s_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


