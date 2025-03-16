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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Optional, Set
from typing_extensions import Self

class ExchangeRecoveryTargetConfig(BaseModel):
    """
    Specifies the target object parameters to recover an Exchange database.
    """ # noqa: E501
    database_directory_location: Optional[StrictStr] = Field(default=None, description="Specifies the directory where to put the database data files. Missing directory will be automatically created.", alias="databaseDirectoryLocation")
    database_name: Optional[StrictStr] = Field(default=None, description="Specifies a new name for the restored database.", alias="databaseName")
    log_directory_location: Optional[StrictStr] = Field(default=None, description="Specifies the directory where to put the database log files. Missing directory will be automatically created.", alias="logDirectoryLocation")
    mount_database: Optional[StrictBool] = Field(default=None, description="Specifies whether to mount the database after successful recovery.", alias="mountDatabase")
    restore_as_recovery_db: Optional[StrictBool] = Field(default=None, description="Specifies whether to restore the Database as Recovery database.", alias="restoreAsRecoveryDB")
    roll_forward_recovery: Optional[StrictBool] = Field(default=None, description="Specifies whether to use the latest logs on Exchange Server to perform roll-forward recovery.", alias="rollForwardRecovery")
    source: Optional[RecoveryObjectIdentifier] = None
    __properties: ClassVar[List[str]] = ["databaseDirectoryLocation", "databaseName", "logDirectoryLocation", "mountDatabase", "restoreAsRecoveryDB", "rollForwardRecovery", "source"]

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
        """Create an instance of ExchangeRecoveryTargetConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # set to None if database_directory_location (nullable) is None
        # and model_fields_set contains the field
        if self.database_directory_location is None and "database_directory_location" in self.model_fields_set:
            _dict['databaseDirectoryLocation'] = None

        # set to None if database_name (nullable) is None
        # and model_fields_set contains the field
        if self.database_name is None and "database_name" in self.model_fields_set:
            _dict['databaseName'] = None

        # set to None if log_directory_location (nullable) is None
        # and model_fields_set contains the field
        if self.log_directory_location is None and "log_directory_location" in self.model_fields_set:
            _dict['logDirectoryLocation'] = None

        # set to None if mount_database (nullable) is None
        # and model_fields_set contains the field
        if self.mount_database is None and "mount_database" in self.model_fields_set:
            _dict['mountDatabase'] = None

        # set to None if restore_as_recovery_db (nullable) is None
        # and model_fields_set contains the field
        if self.restore_as_recovery_db is None and "restore_as_recovery_db" in self.model_fields_set:
            _dict['restoreAsRecoveryDB'] = None

        # set to None if roll_forward_recovery (nullable) is None
        # and model_fields_set contains the field
        if self.roll_forward_recovery is None and "roll_forward_recovery" in self.model_fields_set:
            _dict['rollForwardRecovery'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExchangeRecoveryTargetConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "databaseDirectoryLocation": obj.get("databaseDirectoryLocation"),
            "databaseName": obj.get("databaseName"),
            "logDirectoryLocation": obj.get("logDirectoryLocation"),
            "mountDatabase": obj.get("mountDatabase"),
            "restoreAsRecoveryDB": obj.get("restoreAsRecoveryDB"),
            "rollForwardRecovery": obj.get("rollForwardRecovery"),
            "source": RecoveryObjectIdentifier.from_dict(obj["source"]) if obj.get("source") is not None else None
        })
        return _obj


