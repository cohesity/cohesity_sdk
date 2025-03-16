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
from cohesity_sdk.cluster.models.recover_cassandra_params import RecoverCassandraParams
from typing import Optional, Set
from typing_extensions import Self

class CassandraParams(BaseModel):
    """
    Specifies the recovery options specific to Cassandra environment.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other objects if one of Object failed to recover. Default value is false.", alias="continueOnError")
    is_multi_stage_restore: Optional[StrictBool] = Field(default=None, description="Specifies whether the current recovery operation is a multi-stage restore operation.", alias="isMultiStageRestore")
    recover_cassandra_params: RecoverCassandraParams = Field(alias="recoverCassandraParams")
    recovery_action: StrictStr = Field(description="Specifies the type of recover action to be performed.", alias="recoveryAction")
    __properties: ClassVar[List[str]] = ["continueOnError", "isMultiStageRestore", "recoverCassandraParams", "recoveryAction"]

    @field_validator('recovery_action')
    def recovery_action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RecoverObjects']):
            raise ValueError("must be one of enum values ('RecoverObjects')")
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
        """Create an instance of CassandraParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recover_cassandra_params
        if self.recover_cassandra_params:
            _dict['recoverCassandraParams'] = self.recover_cassandra_params.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if is_multi_stage_restore (nullable) is None
        # and model_fields_set contains the field
        if self.is_multi_stage_restore is None and "is_multi_stage_restore" in self.model_fields_set:
            _dict['isMultiStageRestore'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CassandraParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "isMultiStageRestore": obj.get("isMultiStageRestore"),
            "recoverCassandraParams": RecoverCassandraParams.from_dict(obj["recoverCassandraParams"]) if obj.get("recoverCassandraParams") is not None else None,
            "recoveryAction": obj.get("recoveryAction")
        })
        return _obj


