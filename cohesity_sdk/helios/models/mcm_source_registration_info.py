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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.connection_config import ConnectionConfig
from typing import Optional, Set
from typing_extensions import Self

class McmSourceRegistrationInfo(BaseModel):
    """
    Specifies the registration details and errors occured during registration of a protection source.
    """ # noqa: E501
    connection_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the connection from where this source is reachable.", alias="connectionId")
    connections: Optional[List[ConnectionConfig]] = Field(default=None, description="Specifies the list of connections associated with this source.")
    connector_group_id: Optional[StrictInt] = Field(default=None, description="Specifies the connector group id of connector groups.", alias="connectorGroupId")
    last_refresh_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the registration time of the Source in Unix time epoch in microseconds.", alias="lastRefreshTimeUsecs")
    refresh_error: Optional[StrictStr] = Field(default=None, description="Specifies the error detail occured during the refersh of a protection source.", alias="refreshError")
    registration_error: Optional[StrictStr] = Field(default=None, description="Specifies the error detail occured during the protection source registration.", alias="registrationError")
    registration_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the registration time of the Source in Unix time epoch in microseconds.", alias="registrationTimeUsecs")
    __properties: ClassVar[List[str]] = ["connectionId", "connections", "connectorGroupId", "lastRefreshTimeUsecs", "refreshError", "registrationError", "registrationTimeUsecs"]

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
        """Create an instance of McmSourceRegistrationInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item_connections in self.connections:
                if _item_connections:
                    _items.append(_item_connections.to_dict())
            _dict['connections'] = _items
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

        # set to None if last_refresh_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_refresh_time_usecs is None and "last_refresh_time_usecs" in self.model_fields_set:
            _dict['lastRefreshTimeUsecs'] = None

        # set to None if refresh_error (nullable) is None
        # and model_fields_set contains the field
        if self.refresh_error is None and "refresh_error" in self.model_fields_set:
            _dict['refreshError'] = None

        # set to None if registration_error (nullable) is None
        # and model_fields_set contains the field
        if self.registration_error is None and "registration_error" in self.model_fields_set:
            _dict['registrationError'] = None

        # set to None if registration_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.registration_time_usecs is None and "registration_time_usecs" in self.model_fields_set:
            _dict['registrationTimeUsecs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of McmSourceRegistrationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connectionId": obj.get("connectionId"),
            "connections": [ConnectionConfig.from_dict(_item) for _item in obj["connections"]] if obj.get("connections") is not None else None,
            "connectorGroupId": obj.get("connectorGroupId"),
            "lastRefreshTimeUsecs": obj.get("lastRefreshTimeUsecs"),
            "refreshError": obj.get("refreshError"),
            "registrationError": obj.get("registrationError"),
            "registrationTimeUsecs": obj.get("registrationTimeUsecs")
        })
        return _obj


