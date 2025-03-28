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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.file_extension_filter import FileExtensionFilter
from typing import Set
from typing_extensions import Self

class AntivirusScanConfig(BaseModel):
    """
    Specifies the antivirus scan config settings for this View.
    """ # noqa: E501
    block_access_on_scan_failure: Optional[StrictBool] = Field(default=None, description="Specifies whether block access to the file when antivirus scan fails.", alias="blockAccessOnScanFailure")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether the antivirus service is enabled or not.", alias="isEnabled")
    maximum_scan_file_size: Optional[StrictInt] = Field(default=None, description="Specifies maximum file size that will be sent to antivirus server for scanning. if greater than zero, the file size that exceeds this size would be skipped from virus scan.", alias="maximumScanFileSize")
    scan_filter: Optional[FileExtensionFilter] = Field(default=None, alias="scanFilter")
    scan_on_access: Optional[StrictBool] = Field(default=None, description="Specifies whether to scan a file when it is opened.", alias="scanOnAccess")
    scan_on_close: Optional[StrictBool] = Field(default=None, description="Specifies whether to scan a file when it is closed after modify.", alias="scanOnClose")
    scan_timeout_usecs: Optional[StrictInt] = Field(description="Specifies the maximum amount of time that a scan can take before timing out.", alias="scanTimeoutUsecs")
    __properties: ClassVar[List[str]] = ["blockAccessOnScanFailure", "isEnabled", "maximumScanFileSize", "scanFilter", "scanOnAccess", "scanOnClose", "scanTimeoutUsecs"]

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
        """Create an instance of AntivirusScanConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scan_filter
        if self.scan_filter:
            _dict['scanFilter'] = self.scan_filter.to_dict()
        # set to None if block_access_on_scan_failure (nullable) is None
        # and model_fields_set contains the field
        if self.block_access_on_scan_failure is None and "block_access_on_scan_failure" in self.model_fields_set:
            _dict['blockAccessOnScanFailure'] = None

        # set to None if is_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.is_enabled is None and "is_enabled" in self.model_fields_set:
            _dict['isEnabled'] = None

        # set to None if maximum_scan_file_size (nullable) is None
        # and model_fields_set contains the field
        if self.maximum_scan_file_size is None and "maximum_scan_file_size" in self.model_fields_set:
            _dict['maximumScanFileSize'] = None

        # set to None if scan_on_access (nullable) is None
        # and model_fields_set contains the field
        if self.scan_on_access is None and "scan_on_access" in self.model_fields_set:
            _dict['scanOnAccess'] = None

        # set to None if scan_on_close (nullable) is None
        # and model_fields_set contains the field
        if self.scan_on_close is None and "scan_on_close" in self.model_fields_set:
            _dict['scanOnClose'] = None

        # set to None if scan_timeout_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.scan_timeout_usecs is None and "scan_timeout_usecs" in self.model_fields_set:
            _dict['scanTimeoutUsecs'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AntivirusScanConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "blockAccessOnScanFailure": obj.get("blockAccessOnScanFailure"),
            "isEnabled": obj.get("isEnabled"),
            "maximumScanFileSize": obj.get("maximumScanFileSize"),
            "scanFilter": FileExtensionFilter.from_dict(obj["scanFilter"]) if obj.get("scanFilter") is not None else None,
            "scanOnAccess": obj.get("scanOnAccess"),
            "scanOnClose": obj.get("scanOnClose"),
            "scanTimeoutUsecs": obj.get("scanTimeoutUsecs")
        })
        return _obj


