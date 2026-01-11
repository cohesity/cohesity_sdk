# PostgresSourceRegistrationParams

Specifies parameters to register a Postgres source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**pg_port** | **int** | Specifies the port for the Postgres source. | 
**archive_mode** | **bool** | Specifies the archive mode for the Postgres source. | 
**check_db_connection** | **bool** | Specifies whether to check the database connection for the Postgres source. | 
**hosts** | **[str]** | Specifies the IPs/hostnames for the nodes forming the Postgres source cluster. | 
**script_dir** | **str** | Specifies the directory containing the scripts used to interact with the Postgres source. | 
**source_name** | **str** | Specifies user friendly unique name provided for registering Postgres source. | 
**pg_bin** | **str, none_type** | Specifies the directory containing the PostgreSQL binaries. | [optional] 
**pg_host** | **str, none_type** | Specifies the host for the Postgres source. | [optional] 
**environment_variables** | **[str], none_type** | Specifies the environment variables for the Postgres source. | [optional] 
**kerberos_keytab** | **str, none_type** | Specifies the Kerberos keytab file for the Postgres source authentication. | [optional] 
**kerberos_principal** | **str, none_type** | Specifies the Kerberos principal for the Postgres source authentication. | [optional] 
**ssl_certificate_dir** | **str, none_type** | Specifies the directory containing the SSL certificates for the Postgres source authentication. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


