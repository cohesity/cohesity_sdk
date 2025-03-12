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
from cohesity_sdk.helios.models.ssh_password_credentials import SshPasswordCredentials
from cohesity_sdk.helios.models.ssh_private_key_credentials import SshPrivateKeyCredentials
from typing import Optional, Set
from typing_extensions import Self

class CassandraConnectionParams(BaseModel):
    """
    Specifies the parameters to connect to a Cassandra seed node and fetch information from its cassandra config file.
    """ # noqa: E501
    config_directory: StrictStr = Field(description="Directory path containing Cassandra configuration YAML file.", alias="configDirectory")
    dse_configuration_directory: Optional[StrictStr] = Field(default=None, description="Directory from where DSE specific configuration can be read. This should be set only when you are using the DSE distribution of Cassandra.", alias="dseConfigurationDirectory")
    is_dse_authenticator: StrictBool = Field(description="Set to true if this cluster has DSE Authenticator.", alias="isDseAuthenticator")
    is_dse_tiered_storage: StrictBool = Field(description="Set to true if this cluster has DSE tiered storage.", alias="isDseTieredStorage")
    seed_node: StrictStr = Field(description="Any one seed node of the Cassandra cluster.", alias="seedNode")
    ssh_password_credentials: Optional[SshPasswordCredentials] = Field(default=None, alias="sshPasswordCredentials")
    ssh_private_key_credentials: Optional[SshPrivateKeyCredentials] = Field(default=None, alias="sshPrivateKeyCredentials")
    __properties: ClassVar[List[str]] = ["configDirectory", "dseConfigurationDirectory", "isDseAuthenticator", "isDseTieredStorage", "seedNode", "sshPasswordCredentials", "sshPrivateKeyCredentials"]

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
        """Create an instance of CassandraConnectionParams from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CassandraConnectionParams from a dict"""
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
            "sshPrivateKeyCredentials": SshPrivateKeyCredentials.from_dict(obj["sshPrivateKeyCredentials"]) if obj.get("sshPrivateKeyCredentials") is not None else None
        })
        return _obj


