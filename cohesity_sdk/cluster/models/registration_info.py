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
from typing import Set
from typing_extensions import Self

class RegistrationInfo(BaseModel):
    """
    Specifies the source registration informations.
    """ # noqa: E501
    authentication_status: Optional[StrictStr] = Field(default=None, description="Specifies the status of the authentication during the registration of a Protection Source. 'Pending' indicates the authentication is in progress. 'Scheduled' indicates the authentication is scheduled. 'Finished' indicates the authentication is completed. 'RefreshInProgress' indicates the refresh is in progress.", alias="authenticationStatus")
    last_refreshed_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the source was last refreshed in milliseconds.", alias="lastRefreshedTimeMsecs")
    registration_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the time when the source was registered in milliseconds", alias="registrationTimeMsecs")
    __properties: ClassVar[List[str]] = ["authenticationStatus", "lastRefreshedTimeMsecs", "registrationTimeMsecs"]

    @field_validator('authentication_status')
    def authentication_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Pending', 'Scheduled', 'Finished', 'RefreshInProgress']):
            raise ValueError("must be one of enum values ('Pending', 'Scheduled', 'Finished', 'RefreshInProgress')")
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
        """Create an instance of RegistrationInfo from a JSON string"""
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
            "authentication_status",
            "last_refreshed_time_msecs",
            "registration_time_msecs",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegistrationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authenticationStatus": obj.get("authenticationStatus"),
            "lastRefreshedTimeMsecs": obj.get("lastRefreshedTimeMsecs"),
            "registrationTimeMsecs": obj.get("registrationTimeMsecs")
        })
        return _obj


