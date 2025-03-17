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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.connection_config import ConnectionConfig
from cohesity_sdk.cluster.models.key_value_pair import KeyValuePair
from typing import Set
from typing_extensions import Self

class CommonSourceRegistrationRequestParams(BaseModel):
    """
    Specifies the parameters which are common between all Protection Source registrations.
    """ # noqa: E501
    advanced_configs: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies the advanced configuration for a protection source.", alias="advancedConfigs")
    connection_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user.", alias="connectionId")
    connections: Optional[List[ConnectionConfig]] = Field(default=None, description="Specfies the list of connections for the source.")
    connector_group_id: Optional[StrictInt] = Field(default=None, description="Specifies the connector group id of connector groups.", alias="connectorGroupId")
    encryption_key: Optional[StrictStr] = Field(default=None, description="Specifies the key that user has encrypted the credential with.", alias="encryptionKey")
    environment: Optional[StrictStr] = Field(description="Specifies the environment type of the Protection Source.")
    is_internal_encrypted: Optional[StrictBool] = Field(default=None, description="Specifies if credentials are encrypted by internal key.", alias="isInternalEncrypted")
    name: Optional[StrictStr] = Field(default=None, description="A user specified name for this source.")
    __properties: ClassVar[List[str]] = ["advancedConfigs", "connectionId", "connections", "connectorGroupId", "encryptionKey", "environment", "isInternalEncrypted", "name"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAcropolis', 'kKVM', 'kAWS', 'kGCP', 'kAzure', 'kPhysical', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kGPFS', 'kElastifile', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSQL', 'kOracle', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAcropolis', 'kKVM', 'kAWS', 'kGCP', 'kAzure', 'kPhysical', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kGPFS', 'kElastifile', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSQL', 'kOracle', 'kSfdc')")
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
        """Create an instance of CommonSourceRegistrationRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in advanced_configs (list)
        _items = []
        if self.advanced_configs:
            for _item_advanced_configs in self.advanced_configs:
                if _item_advanced_configs:
                    _items.append(_item_advanced_configs.to_dict())
            _dict['advancedConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item_connections in self.connections:
                if _item_connections:
                    _items.append(_item_connections.to_dict())
            _dict['connections'] = _items
        # set to None if advanced_configs (nullable) is None
        # and model_fields_set contains the field
        if self.advanced_configs is None and "advanced_configs" in self.model_fields_set:
            _dict['advancedConfigs'] = None

        # set to None if connection_id (nullable) is None
        # and model_fields_set contains the field
        if self.connection_id is None and "connection_id" in self.model_fields_set:
            _dict['connectionId'] = None

        # set to None if connections (nullable) is None
        # and model_fields_set contains the field
        if self.connections is None and "connections" in self.model_fields_set:
            _dict['connections'] = None

        # set to None if connector_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.connector_group_id is None and "connector_group_id" in self.model_fields_set:
            _dict['connectorGroupId'] = None

        # set to None if encryption_key (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_key is None and "encryption_key" in self.model_fields_set:
            _dict['encryptionKey'] = None

        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if is_internal_encrypted (nullable) is None
        # and model_fields_set contains the field
        if self.is_internal_encrypted is None and "is_internal_encrypted" in self.model_fields_set:
            _dict['isInternalEncrypted'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonSourceRegistrationRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "advancedConfigs": [KeyValuePair.from_dict(_item) for _item in obj["advancedConfigs"]] if obj.get("advancedConfigs") is not None else None,
            "connectionId": obj.get("connectionId"),
            "connections": [ConnectionConfig.from_dict(_item) for _item in obj["connections"]] if obj.get("connections") is not None else None,
            "connectorGroupId": obj.get("connectorGroupId"),
            "encryptionKey": obj.get("encryptionKey"),
            "environment": obj.get("environment"),
            "isInternalEncrypted": obj.get("isInternalEncrypted"),
            "name": obj.get("name")
        })
        return _obj


