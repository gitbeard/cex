class FileInfo < ActiveRecord::Base
  attr_accessible :date_modified, :date_uploaded, :filename
end
