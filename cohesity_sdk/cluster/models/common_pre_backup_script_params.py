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
from typing_extensions import Annotated
from typing import Set
from typing_extensions import Self

class CommonPreBackupScriptParams(BaseModel):
    """
    Specifies the common params for PreBackup scripts.
    """ # noqa: E501
    is_active: Optional[StrictBool] = Field(default=None, description="Specifies whether the script should be enabled, default value set to true.", alias="isActive")
    params: Optional[StrictStr] = Field(default=None, description="Specifies the arguments or parameters and values to pass into the remote script. For example if the script expects values for the 'database' and 'user' parameters, specify the parameters and values using the following string: \"database=myDatabase user=me\".")
    path: StrictStr = Field(description="Specifies the absolute path to the script on the remote host.")
    timeout_secs: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Specifies the timeout of the script in seconds. The script will be killed if it exceeds this value. By default, no timeout will occur if left empty.", alias="timeoutSecs")
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies if the script needs to continue even if there is an occurence of an error. If this flag is set to true, then Backup Run will start even if the pre backup script fails. If not specified or false, then backup run will not start when script fails.", alias="continueOnError")
    __properties: ClassVar[List[str]] = ["isActive", "params", "path", "timeoutSecs", "continueOnError"]

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
        """Create an instance of CommonPreBackupScriptParams from a JSON string"""
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
        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['isActive'] = None

        # set to None if params (nullable) is None
        # and model_fields_set contains the field
        if self.params is None and "params" in self.model_fields_set:
            _dict['params'] = None

        # set to None if timeout_secs (nullable) is None
        # and model_fields_set contains the field
        if self.timeout_secs is None and "timeout_secs" in self.model_fields_set:
            _dict['timeoutSecs'] = None

        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonPreBackupScriptParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isActive": obj.get("isActive"),
            "params": obj.get("params"),
            "path": obj.get("path"),
            "timeoutSecs": obj.get("timeoutSecs"),
            "continueOnError": obj.get("continueOnError")
        })
        return _obj


