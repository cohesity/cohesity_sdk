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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.hbase_source_registration_params_all_of_ssh_private_key_credentials import HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials
from cohesity_sdk.helios.models.hive_source_registration_params_all_of_ssh_password_credentials import HiveSourceRegistrationParamsAllOfSshPasswordCredentials
from typing import Set
from typing_extensions import Self

class HiveSourceRegistrationParams(BaseModel):
    """
    Specifies parameters to register Hive source.
    """ # noqa: E501
    auth_type: Optional[StrictStr] = Field(default=None, description="Authentication type.", alias="authType")
    metastore_address: Optional[StrictStr] = Field(default=None, description="The MetastoreAddress for this Hive.", alias="metastoreAddress")
    metastore_port: Optional[StrictInt] = Field(default=None, description="The MetastorePort for this Hive.", alias="metastorePort")
    configuration_directory: StrictStr = Field(description="The directory containing the hive-site.xml.", alias="configurationDirectory")
    hdfs_source_registration_id: StrictInt = Field(description="Protection Source registration id of the HDFS on which this Hive is running.", alias="hdfsSourceRegistrationID")
    host: StrictStr = Field(description="IP or hostname of any host from which the Hive configuration file hive-site.xml can be read.")
    kerberos_principal: Optional[StrictStr] = Field(default=None, description="The kerberos principal to be used to connect to this Hive source.", alias="kerberosPrincipal")
    ssh_password_credentials: Optional[HiveSourceRegistrationParamsAllOfSshPasswordCredentials] = Field(default=None, alias="sshPasswordCredentials")
    ssh_private_key_credentials: Optional[HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials] = Field(default=None, alias="sshPrivateKeyCredentials")
    __properties: ClassVar[List[str]] = ["authType", "metastoreAddress", "metastorePort", "configurationDirectory", "hdfsSourceRegistrationID", "host", "kerberosPrincipal", "sshPasswordCredentials", "sshPrivateKeyCredentials"]

    @field_validator('auth_type')
    def auth_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['KERBEROS', 'NONE']):
            raise ValueError("must be one of enum values ('KERBEROS', 'NONE')")
        return value

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
        """Create an instance of HiveSourceRegistrationParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "auth_type",
            "metastore_address",
            "metastore_port",
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
        # set to None if auth_type (nullable) is None
        # and model_fields_set contains the field
        if self.auth_type is None and "auth_type" in self.model_fields_set:
            _dict['authType'] = None

        # set to None if kerberos_principal (nullable) is None
        # and model_fields_set contains the field
        if self.kerberos_principal is None and "kerberos_principal" in self.model_fields_set:
            _dict['kerberosPrincipal'] = None

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
        """Create an instance of HiveSourceRegistrationParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authType": obj.get("authType"),
            "metastoreAddress": obj.get("metastoreAddress"),
            "metastorePort": obj.get("metastorePort"),
            "configurationDirectory": obj.get("configurationDirectory"),
            "hdfsSourceRegistrationID": obj.get("hdfsSourceRegistrationID"),
            "host": obj.get("host"),
            "kerberosPrincipal": obj.get("kerberosPrincipal"),
            "sshPasswordCredentials": HiveSourceRegistrationParamsAllOfSshPasswordCredentials.from_dict(obj["sshPasswordCredentials"]) if obj.get("sshPasswordCredentials") is not None else None,
            "sshPrivateKeyCredentials": HbaseSourceRegistrationParamsAllOfSshPrivateKeyCredentials.from_dict(obj["sshPrivateKeyCredentials"]) if obj.get("sshPrivateKeyCredentials") is not None else None
        })
        return _obj


