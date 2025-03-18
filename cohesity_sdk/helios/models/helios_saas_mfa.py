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
from cohesity_sdk.helios.models.mfa_opt_out_config import MfaOptOutConfig
from typing import Set
from typing_extensions import Self

class HeliosSaasMfa(BaseModel):
    """
    Specifies MFA configuration for an account in the Helios SaaS environment.
    """ # noqa: E501
    grace_period_end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of the grace period for this customer in microseconds since the epoch.", alias="gracePeriodEndTimeUsecs")
    grace_period_start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of the grace period for this customer in microseconds since the epoch.", alias="gracePeriodStartTimeUsecs")
    mfa_status: Optional[StrictStr] = Field(description="Specifies the current MFA status.", alias="mfaStatus")
    opt_out_config: Optional[MfaOptOutConfig] = Field(default=None, alias="optOutConfig")
    __properties: ClassVar[List[str]] = ["gracePeriodEndTimeUsecs", "gracePeriodStartTimeUsecs", "mfaStatus", "optOutConfig"]

    @field_validator('mfa_status')
    def mfa_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['OptIn', 'OptOut', 'Pending', 'Unknown']):
            raise ValueError("must be one of enum values ('OptIn', 'OptOut', 'Pending', 'Unknown')")
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
        """Create an instance of HeliosSaasMfa from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "grace_period_end_time_usecs",
            "grace_period_start_time_usecs",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of opt_out_config
        if self.opt_out_config:
            _dict['optOutConfig'] = self.opt_out_config.to_dict()
        # set to None if grace_period_end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.grace_period_end_time_usecs is None and "grace_period_end_time_usecs" in self.model_fields_set:
            _dict['gracePeriodEndTimeUsecs'] = None

        # set to None if grace_period_start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.grace_period_start_time_usecs is None and "grace_period_start_time_usecs" in self.model_fields_set:
            _dict['gracePeriodStartTimeUsecs'] = None

        # set to None if mfa_status (nullable) is None
        # and model_fields_set contains the field
        if self.mfa_status is None and "mfa_status" in self.model_fields_set:
            _dict['mfaStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosSaasMfa from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gracePeriodEndTimeUsecs": obj.get("gracePeriodEndTimeUsecs"),
            "gracePeriodStartTimeUsecs": obj.get("gracePeriodStartTimeUsecs"),
            "mfaStatus": obj.get("mfaStatus"),
            "optOutConfig": MfaOptOutConfig.from_dict(obj["optOutConfig"]) if obj.get("optOutConfig") is not None else None
        })
        return _obj


