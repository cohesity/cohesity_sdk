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
from cohesity_sdk.helios.models.exchange_database_recovery_target_config import ExchangeDatabaseRecoveryTargetConfig
from cohesity_sdk.helios.models.recovery_object_identifier import RecoveryObjectIdentifier
from cohesity_sdk.helios.models.view_options import ViewOptions
from typing import Set
from typing_extensions import Self

class ExchangeRecoverDatabaseParams(BaseModel):
    """
    Specifies the parameters to recover an Exchange database. database.
    """ # noqa: E501
    database_source: RecoveryObjectIdentifier = Field(alias="databaseSource")
    recover_to_new_source: StrictBool = Field(description="Specifies the parameter whether the recovery should be performed to a new or an existing Source Target.", alias="recoverToNewSource")
    recovery_target_config: Optional[ExchangeDatabaseRecoveryTargetConfig] = Field(default=None, alias="recoveryTargetConfig")
    restore_type: Optional[StrictStr] = Field(description="Specifies the type of exchange restore.", alias="restoreType")
    view_options: Optional[ViewOptions] = Field(default=None, alias="viewOptions")
    __properties: ClassVar[List[str]] = ["databaseSource", "recoverToNewSource", "recoveryTargetConfig", "restoreType", "viewOptions"]

    @field_validator('restore_type')
    def restore_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RestoreView']):
            raise ValueError("must be one of enum values ('RestoreView')")
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
        """Create an instance of ExchangeRecoverDatabaseParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of database_source
        if self.database_source:
            _dict['databaseSource'] = self.database_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recovery_target_config
        if self.recovery_target_config:
            _dict['recoveryTargetConfig'] = self.recovery_target_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of view_options
        if self.view_options:
            _dict['viewOptions'] = self.view_options.to_dict()
        # set to None if restore_type (nullable) is None
        # and model_fields_set contains the field
        if self.restore_type is None and "restore_type" in self.model_fields_set:
            _dict['restoreType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExchangeRecoverDatabaseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "databaseSource": RecoveryObjectIdentifier.from_dict(obj["databaseSource"]) if obj.get("databaseSource") is not None else None,
            "recoverToNewSource": obj.get("recoverToNewSource"),
            "recoveryTargetConfig": ExchangeDatabaseRecoveryTargetConfig.from_dict(obj["recoveryTargetConfig"]) if obj.get("recoveryTargetConfig") is not None else None,
            "restoreType": obj.get("restoreType"),
            "viewOptions": ViewOptions.from_dict(obj["viewOptions"]) if obj.get("viewOptions") is not None else None
        })
        return _obj


