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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.cluster.models.alert_target import AlertTarget
from typing import Set
from typing_extensions import Self

class ProtectionGroupAlertingPolicy(BaseModel):
    """
    Specifies a policy for alerting users of the status of a Protection Group.
    """ # noqa: E501
    alert_targets: Optional[List[AlertTarget]] = Field(default=None, description="Specifies a list of targets to receive the alerts.", alias="alertTargets")
    backup_run_status: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="Specifies the run status for which the user would like to receive alerts.", alias="backupRunStatus")
    raise_object_level_failure_alert: Optional[StrictBool] = Field(default=None, description="Specifies whether object level alerts are raised for backup failures after the backup run.", alias="raiseObjectLevelFailureAlert")
    raise_object_level_failure_alert_after_each_attempt: Optional[StrictBool] = Field(default=None, description="Specifies whether object level alerts are raised for backup failures after each backup attempt.", alias="raiseObjectLevelFailureAlertAfterEachAttempt")
    raise_object_level_failure_alert_after_last_attempt: Optional[StrictBool] = Field(default=None, description="Specifies whether object level alerts are raised for backup failures after last backup attempt.", alias="raiseObjectLevelFailureAlertAfterLastAttempt")
    __properties: ClassVar[List[str]] = ["alertTargets", "backupRunStatus", "raiseObjectLevelFailureAlert", "raiseObjectLevelFailureAlertAfterEachAttempt", "raiseObjectLevelFailureAlertAfterLastAttempt"]

    @field_validator('backup_run_status')
    def backup_run_status_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['kSuccess', 'kFailure', 'kSlaViolation', 'kWarning']):
                raise ValueError("each list item must be one of ('kSuccess', 'kFailure', 'kSlaViolation', 'kWarning')")
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
        """Create an instance of ProtectionGroupAlertingPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in alert_targets (list)
        _items = []
        if self.alert_targets:
            for _item_alert_targets in self.alert_targets:
                if _item_alert_targets:
                    _items.append(_item_alert_targets.to_dict())
            _dict['alertTargets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProtectionGroupAlertingPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertTargets": [AlertTarget.from_dict(_item) for _item in obj["alertTargets"]] if obj.get("alertTargets") is not None else None,
            "backupRunStatus": obj.get("backupRunStatus"),
            "raiseObjectLevelFailureAlert": obj.get("raiseObjectLevelFailureAlert"),
            "raiseObjectLevelFailureAlertAfterEachAttempt": obj.get("raiseObjectLevelFailureAlertAfterEachAttempt"),
            "raiseObjectLevelFailureAlertAfterLastAttempt": obj.get("raiseObjectLevelFailureAlertAfterLastAttempt")
        })
        return _obj


