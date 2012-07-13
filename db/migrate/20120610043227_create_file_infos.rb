class CreateFileInfos < ActiveRecord::Migration
  def change
    create_table :file_infos do |t|
      t.string :filename
      t.datetime :date_modified
      t.datetime :date_uploaded

      t.timestamps
    end
  end
end
