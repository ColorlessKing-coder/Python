from HostDiscovery import  ParserHostDiscovery,PortScanner, HostDiscoveryWithArp,HostDiscoveryWithIcmpFourPackReceive ,HosDiscoveryOnePackReceive


if __name__ == '__main__':
    args = ParserHostDiscovery()
    
    if args.type == 'ARP':
        HostDiscoveryWithArp(args.ip_address , args.subnet_mask , args.count , args.timeout , args.verbose , args.port_range , args.port_type)
    elif args.type == 'ICMP4Rec':
        HostDiscoveryWithIcmpFourPackReceive(args.ip_address , args.timeout , args.port_range , args.verbose , args.port_type)
    elif args.type == 'ICMP1Rec':
        HosDiscoveryOnePackReceive(args.ip_address , args.timeout , args.port_range , args.verbose , args.port_type)
    else:
        print("Please choose a valid option.")
