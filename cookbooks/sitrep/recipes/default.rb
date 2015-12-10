##
# This file loads the correct packages and sets up the files
# as required

execute "apt-get-update-periodic" do
    command "apt-get update"
    ignore_failure true
    only_if do
    File.exists?('/var/lib/apt/periodic/update-success-stamp') &&
        File.mtime('/var/lib/apt/periodic/update-success-stamp') < Time.now - 86400
    end
end

# Install the packages required
package "git"
package "mongodb"
package "python"
package "python-pip"

# Configure the bash alias file
cookbook_file '.bash_aliases' do
    path '/home/vagrant/.bash_aliases'
    mode '600'
    owner 'vagrant'
    action [ :delete, :create ]
end
