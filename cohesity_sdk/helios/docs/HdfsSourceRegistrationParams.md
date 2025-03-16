# HdfsSourceRegistrationParams

Specifies parameters to register an HDFS source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authentication type. | [optional] [readonly] 
**namenode_address** | **str** | The HDFS Namenode IP or hostname. | [optional] [readonly] 
**webhdfs_port** | **int** | The HDFS WebHDFS port. | [optional] [readonly] 
**configuration_directory** | **str** | The directory containing the core-site.xml and hdfs-site.xml configuration files. | 
**hadoop_distribution** | **str** | The hadoop distribution for this cluster. This can be either &#39;CDH&#39; or &#39;HDP&#39; | 
**hadoop_version** | **str** | The hadoop version for this cluster. | 
**host** | **str** | IP or hostname of any host from which the HDFS configuration files core-site.xml and hdfs-site.xml can be read. | 
**kerberos_principal** | **str** | The kerberos principal to be used to connect to this HDFS source. | [optional] 
**ssh_password_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPasswordCredentials**](HbaseSourceRegistrationParamsAllOfSshPasswordCredentials.md) |  | [optional] 
**ssh_private_key_credentials** | [**HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials**](HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.hdfs_source_registration_params import HdfsSourceRegistrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of HdfsSourceRegistrationParams from a JSON string
hdfs_source_registration_params_instance = HdfsSourceRegistrationParams.from_json(json)
# print the JSON string representation of the object
print(HdfsSourceRegistrationParams.to_json())

# convert the object into a dict
hdfs_source_registration_params_dict = hdfs_source_registration_params_instance.to_dict()
# create an instance of HdfsSourceRegistrationParams from a dict
hdfs_source_registration_params_from_dict = HdfsSourceRegistrationParams.from_dict(hdfs_source_registration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


