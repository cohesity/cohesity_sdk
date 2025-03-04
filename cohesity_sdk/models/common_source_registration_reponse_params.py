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
from cohesity_sdk.models.connection_config import ConnectionConfig
from cohesity_sdk.models.key_value_pair import KeyValuePair
from cohesity_sdk.models.object import Object
from typing import Optional, Set
from typing_extensions import Self

class CommonSourceRegistrationReponseParams(BaseModel):
    """
    Specifies the parameters which are common between all Protection Source registrations.
    """ # noqa: E501
    authentication_status: Optional[StrictStr] = Field(default=None, description="Specifies the status of the authentication during the registration of a Protection Source. 'Pending' indicates the authentication is in progress. 'Scheduled' indicates the authentication is scheduled. 'Finished' indicates the authentication is completed. 'RefreshInProgress' indicates the refresh is in progress.", alias="authenticationStatus")
    last_refreshed_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the source was last refreshed in milliseconds.", alias="lastRefreshedTimeMsecs")
    registration_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the source was registered in milliseconds", alias="registrationTimeMsecs")
    advanced_configs: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies the advanced configuration for a protection source.", alias="advancedConfigs")
    connection_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. This field will be depricated in future. Use connections field.", alias="connectionId")
    connections: Optional[List[ConnectionConfig]] = Field(default=None, description="Specfies the list of connections for the source.")
    connector_group_id: Optional[StrictInt] = Field(default=None, description="Specifies the connector group id of connector groups.", alias="connectorGroupId")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment type of the Protection Source.")
    id: Optional[StrictInt] = Field(default=None, description="Source Registration ID. This can be used to retrieve, edit or delete the source registration.")
    name: Optional[StrictStr] = Field(default=None, description="The user specified name for this source.")
    source_id: Optional[StrictInt] = Field(default=None, description="ID of top level source object discovered after the registration.", alias="sourceId")
    source_info: Optional[Object] = Field(default=None, alias="sourceInfo")
    __properties: ClassVar[List[str]] = ["authenticationStatus", "lastRefreshedTimeMsecs", "registrationTimeMsecs", "advancedConfigs", "connectionId", "connections", "connectorGroupId", "environment", "id", "name", "sourceId", "sourceInfo"]

    @field_validator('authentication_status')
    def authentication_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Pending', 'Scheduled', 'Finished', 'RefreshInProgress']):
            raise ValueError("must be one of enum values ('Pending', 'Scheduled', 'Finished', 'RefreshInProgress')")
        return value

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
        """Create an instance of CommonSourceRegistrationReponseParams from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "authentication_status",
            "last_refreshed_time_msecs",
            "registration_time_msecs",
            "id",
            "source_id",
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
        # override the default output from pydantic by calling `to_dict()` of source_info
        if self.source_info:
            _dict['sourceInfo'] = self.source_info.to_dict()
        # set to None if authentication_status (nullable) is None
        # and model_fields_set contains the field
        if self.authentication_status is None and "authentication_status" in self.model_fields_set:
            _dict['authenticationStatus'] = None

        # set to None if last_refreshed_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_refreshed_time_msecs is None and "last_refreshed_time_msecs" in self.model_fields_set:
            _dict['lastRefreshedTimeMsecs'] = None

        # set to None if registration_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.registration_time_msecs is None and "registration_time_msecs" in self.model_fields_set:
            _dict['registrationTimeMsecs'] = None

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

        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonSourceRegistrationReponseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authenticationStatus": obj.get("authenticationStatus"),
            "lastRefreshedTimeMsecs": obj.get("lastRefreshedTimeMsecs"),
            "registrationTimeMsecs": obj.get("registrationTimeMsecs"),
            "advancedConfigs": [KeyValuePair.from_dict(_item) for _item in obj["advancedConfigs"]] if obj.get("advancedConfigs") is not None else None,
            "connectionId": obj.get("connectionId"),
            "connections": [ConnectionConfig.from_dict(_item) for _item in obj["connections"]] if obj.get("connections") is not None else None,
            "connectorGroupId": obj.get("connectorGroupId"),
            "environment": obj.get("environment"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "sourceId": obj.get("sourceId"),
            "sourceInfo": Object.from_dict(obj["sourceInfo"]) if obj.get("sourceInfo") is not None else None
        })
        return _obj


