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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.local_user_update_params import LocalUserUpdateParams
from typing import Set
from typing_extensions import Self

class UpdateUserParameters(BaseModel):
    """
    Specifies User properties to update.
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Specifies the description of the User.")
    effective_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the epoch time in milliseconds since when the user can login.", alias="effectiveTimeMsecs")
    expiry_time_msecs: Optional[StrictInt] = Field(default=None, description="Specifies the epoch time in milliseconds when the user expires. Post expiry the user cannot access Cohesity cluster.", alias="expiryTimeMsecs")
    locked: Optional[StrictBool] = Field(default=None, description="Specifies whether the User is locked.")
    restricted: Optional[StrictBool] = Field(default=None, description="Specifies whether the User is restricted. A restricted user can only view & manage the objects it has permissions to.")
    roles: Optional[List[StrictStr]] = Field(default=None, description="Specifies the Cohesity roles to associate with the user. The Cohesity roles determine privileges on the Cohesity Cluster for this user.")
    local_user_params: Optional[LocalUserUpdateParams] = Field(default=None, alias="localUserParams")
    __properties: ClassVar[List[str]] = ["description", "effectiveTimeMsecs", "expiryTimeMsecs", "locked", "restricted", "roles", "localUserParams"]

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
        """Create an instance of UpdateUserParameters from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of local_user_params
        if self.local_user_params:
            _dict['localUserParams'] = self.local_user_params.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if effective_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.effective_time_msecs is None and "effective_time_msecs" in self.model_fields_set:
            _dict['effectiveTimeMsecs'] = None

        # set to None if expiry_time_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_time_msecs is None and "expiry_time_msecs" in self.model_fields_set:
            _dict['expiryTimeMsecs'] = None

        # set to None if locked (nullable) is None
        # and model_fields_set contains the field
        if self.locked is None and "locked" in self.model_fields_set:
            _dict['locked'] = None

        # set to None if restricted (nullable) is None
        # and model_fields_set contains the field
        if self.restricted is None and "restricted" in self.model_fields_set:
            _dict['restricted'] = None

        # set to None if roles (nullable) is None
        # and model_fields_set contains the field
        if self.roles is None and "roles" in self.model_fields_set:
            _dict['roles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateUserParameters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "effectiveTimeMsecs": obj.get("effectiveTimeMsecs"),
            "expiryTimeMsecs": obj.get("expiryTimeMsecs"),
            "locked": obj.get("locked"),
            "restricted": obj.get("restricted"),
            "roles": obj.get("roles"),
            "localUserParams": LocalUserUpdateParams.from_dict(obj["localUserParams"]) if obj.get("localUserParams") is not None else None
        })
        return _obj


