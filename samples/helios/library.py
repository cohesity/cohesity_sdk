from cohesity_sdk.helios_mcm.v2.model.source_registration_request_params import (
    SourceRegistrationRequestParams,
)
from cohesity_sdk.helios_mcm.v2.model.vmware_source_registration_params import (
    VmwareSourceRegistrationParams,
)
from cohesity_sdk.helios_mcm.v2.model.vcenter_registration_params import (
    VcenterRegistrationParams,
)
from cohesity_sdk.helios_mcm.v2.model.physical_source_registration_params import (
    PhysicalSourceRegistrationParams,
)


def register_vmware_source(client, source, username, password):
    """
    Function to register a VMware source
    : return source Id
    """
    payload = SourceRegistrationRequestParams(
        environment="kVMware",
        vmware_params=VmwareSourceRegistrationParams(
            type="kVCenter",
            v_center_params=VcenterRegistrationParams(
                username=username, password=password, endpoint=source
            ),
        ),
    )
    response = client.source.register_protection_source(payload)
    return response.id


def register_physical_source(client, source):
    """
    Function to register a physical source
    : return sourceId
    """
    try:
        payload = SourceRegistrationRequestParams(
            environment="kPhysical",
            physical_params=PhysicalSourceRegistrationParams(
                endpoint=source,
                force_register=True,
                physical_type="kHost",
                host_type="kLinux",
            ),
        )
        response = client.source.register_protection_source(payload)
        return response.id
    except Exception as err:
        print(err)
