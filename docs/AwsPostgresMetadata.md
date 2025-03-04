# AwsPostgresMetadata

Specifies the metadata types and values of aws postgres.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_type** | **str** | Specifies the type of metadata being sent in the request. | 
**standard_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.aws_postgres_metadata import AwsPostgresMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPostgresMetadata from a JSON string
aws_postgres_metadata_instance = AwsPostgresMetadata.from_json(json)
# print the JSON string representation of the object
print(AwsPostgresMetadata.to_json())

# convert the object into a dict
aws_postgres_metadata_dict = aws_postgres_metadata_instance.to_dict()
# create an instance of AwsPostgresMetadata from a dict
aws_postgres_metadata_from_dict = AwsPostgresMetadata.from_dict(aws_postgres_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


