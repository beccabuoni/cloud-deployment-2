"""Create multiple nodes and assign information with loops.
"""

import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.igext

# Define parameters
portal.context.defineParameter( "n", "Number of VMs", portal.ParameterType.INTEGER, 4 )

# Get user specified values
params = portal.context.bindParameters()

#Create portal context
pc = portal.Context()

# Create a Request object to start building the RSpec
request = pc.makeRequestRSpec()

# Check parameters
if params.n < 1 or params.n > 4:
    pc.reportError( portal.ParameterError( "You must choose at least 1 and no more than 4 VMs." ) )

link = request.LAN("lan")

# Use a loop to create and assign values to XenVM nodes
for i in range( params.n ):
    node = request.XenVM( "node-" + str( i + 1) )
    node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:CENTOS7-64-STD"
    if (i + 1) == 1:
        node.routable_control_ip = True
    inface = node.addInterface("if1")
    
    # Assign component id and IPv4 address
    inface.component_id = "eth1"
    inface.addAddress(rspec.IPv4Address("192.168.1." + str( i + 1 ), "255.255.255.0"))

    link.addInterface(inface)

pc.printRequestRSpec()
