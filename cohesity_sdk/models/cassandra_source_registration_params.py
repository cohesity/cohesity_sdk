# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.cassandra_source_registration_params_all_of_cassandra_credentials import CassandraSourceRegistrationParamsAllOfCassandraCredentials
from cohesity_sdk.models.cassandra_source_registration_params_all_of_jmx_credentials import CassandraSourceRegistrationParamsAllOfJmxCredentials
from cohesity_sdk.models.dse_solr_info import DSESolrInfo
from cohesity_sdk.models.ssh_password_credentials import SshPasswordCredentials
from cohesity_sdk.models.ssh_private_key_credentials import SshPrivateKeyCredentials
from typing import Optional, Set
from typing_extensions import Self

class CassandraSourceRegistrationParams(BaseModel):
    """
    Specifies parameters to register cassandra source.
    """ # noqa: E501
    config_directory: StrictStr = Field(description="Directory path containing Cassandra configuration YAML file.", alias="configDirectory")
    dse_configuration_directory: Optional[StrictStr] = Field(default=None, description="Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra.", alias="dseConfigurationDirectory")
    is_dse_authenticator: StrictBool = Field(description="Set to true if this cluster has DSE Authenticator.", alias="isDseAuthenticator")
    is_dse_tiered_storage: StrictBool = Field(description="Set to true if this cluster has DSE tiered storage.", alias="isDseTieredStorage")
    seed_node: StrictStr = Field(description="Any one seed node of the Cassandra cluster.", alias="seedNode")
    ssh_password_credentials: Optional[SshPasswordCredentials] = Field(default=None, alias="sshPasswordCredentials")
    ssh_private_key_credentials: Optional[SshPrivateKeyCredentials] = Field(default=None, alias="sshPrivateKeyCredentials")
    cassandra_credentials: Optional[CassandraSourceRegistrationParamsAllOfCassandraCredentials] = Field(default=None, alias="cassandraCredentials")
    commit_log_backup_location: Optional[StrictStr] = Field(default=None, description="Commit Logs backup location on cassandra nodes", alias="commitLogBackupLocation")
    data_center_names: Optional[List[StrictStr]] = Field(default=None, description="Data centers for this cluster.", alias="dataCenterNames")
    dse_solr_info: Optional[DSESolrInfo] = Field(default=None, alias="dseSolrInfo")
    jmx_credentials: Optional[CassandraSourceRegistrationParamsAllOfJmxCredentials] = Field(default=None, alias="jmxCredentials")
    kerberos_principal: Optional[StrictStr] = Field(default=None, description="Principal for the kerberos connection. (This is required only if your Cassandra has Kerberos authentication. Please refer to the user guide.)", alias="kerberosPrincipal")
    __properties: ClassVar[List[str]] = ["configDirectory", "dseConfigurationDirectory", "isDseAuthenticator", "isDseTieredStorage", "seedNode", "sshPasswordCredentials", "sshPrivateKeyCredentials", "cassandraCredentials", "commitLogBackupLocation", "dataCenterNames", "dseSolrInfo", "jmxCredentials", "kerberosPrincipal"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CassandraSourceRegistrationParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of ssh_password_credentials
        if self.ssh_password_credentials:
            _dict['sshPasswordCredentials'] = self.ssh_password_credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ssh_private_key_credentials
        if self.ssh_private_key_credentials:
            _dict['sshPrivateKeyCredentials'] = self.ssh_private_key_credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cassandra_credentials
        if self.cassandra_credentials:
            _dict['cassandraCredentials'] = self.cassandra_credentials.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dse_solr_info
        if self.dse_solr_info:
            _dict['dseSolrInfo'] = self.dse_solr_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jmx_credentials
        if self.jmx_credentials:
            _dict['jmxCredentials'] = self.jmx_credentials.to_dict()
        # set to None if dse_configuration_directory (nullable) is None
        # and model_fields_set contains the field
        if self.dse_configuration_directory is None and "dse_configuration_directory" in self.model_fields_set:
            _dict['dseConfigurationDirectory'] = None

        # set to None if ssh_password_credentials (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_password_credentials is None and "ssh_password_credentials" in self.model_fields_set:
            _dict['sshPasswordCredentials'] = None

        # set to None if ssh_private_key_credentials (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_private_key_credentials is None and "ssh_private_key_credentials" in self.model_fields_set:
            _dict['sshPrivateKeyCredentials'] = None

        # set to None if cassandra_credentials (nullable) is None
        # and model_fields_set contains the field
        if self.cassandra_credentials is None and "cassandra_credentials" in self.model_fields_set:
            _dict['cassandraCredentials'] = None

        # set to None if commit_log_backup_location (nullable) is None
        # and model_fields_set contains the field
        if self.commit_log_backup_location is None and "commit_log_backup_location" in self.model_fields_set:
            _dict['commitLogBackupLocation'] = None

        # set to None if jmx_credentials (nullable) is None
        # and model_fields_set contains the field
        if self.jmx_credentials is None and "jmx_credentials" in self.model_fields_set:
            _dict['jmxCredentials'] = None

        # set to None if kerberos_principal (nullable) is None
        # and model_fields_set contains the field
        if self.kerberos_principal is None and "kerberos_principal" in self.model_fields_set:
            _dict['kerberosPrincipal'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CassandraSourceRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configDirectory": obj.get("configDirectory"),
            "dseConfigurationDirectory": obj.get("dseConfigurationDirectory"),
            "isDseAuthenticator": obj.get("isDseAuthenticator"),
            "isDseTieredStorage": obj.get("isDseTieredStorage"),
            "seedNode": obj.get("seedNode"),
            "sshPasswordCredentials": SshPasswordCredentials.from_dict(obj["sshPasswordCredentials"]) if obj.get("sshPasswordCredentials") is not None else None,
            "sshPrivateKeyCredentials": SshPrivateKeyCredentials.from_dict(obj["sshPrivateKeyCredentials"]) if obj.get("sshPrivateKeyCredentials") is not None else None,
            "cassandraCredentials": CassandraSourceRegistrationParamsAllOfCassandraCredentials.from_dict(obj["cassandraCredentials"]) if obj.get("cassandraCredentials") is not None else None,
            "commitLogBackupLocation": obj.get("commitLogBackupLocation"),
            "dataCenterNames": obj.get("dataCenterNames"),
            "dseSolrInfo": DSESolrInfo.from_dict(obj["dseSolrInfo"]) if obj.get("dseSolrInfo") is not None else None,
            "jmxCredentials": CassandraSourceRegistrationParamsAllOfJmxCredentials.from_dict(obj["jmxCredentials"]) if obj.get("jmxCredentials") is not None else None,
            "kerberosPrincipal": obj.get("kerberosPrincipal")
        })
        return _obj


