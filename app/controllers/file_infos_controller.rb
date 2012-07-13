class FileInfosController < ApplicationController
  # GET /file_infos
  # GET /file_infos.json
  def index
    @file_infos = FileInfo.all

    respond_to do |format|
      format.html # index.html.erb
      format.json { render json: @file_infos }
    end
  end

  # GET /file_infos/1
  # GET /file_infos/1.json
  def show
    @file_info = FileInfo.find(params[:id])

    respond_to do |format|
      format.html # show.html.erb
      format.json { render json: @file_info }
    end
  end

  # GET /file_infos/new
  # GET /file_infos/new.json
  def new
    @file_info = FileInfo.new

    respond_to do |format|
      format.html # new.html.erb
      format.json { render json: @file_info }
    end
  end

  # GET /file_infos/1/edit
  def edit
    @file_info = FileInfo.find(params[:id])
  end

  # POST /file_infos
  # POST /file_infos.json
  def create
    @file_info = FileInfo.new(params[:file_info])

    respond_to do |format|
      if @file_info.save
        format.html { redirect_to @file_info, notice: 'File info was successfully created.' }
        format.json { render json: @file_info, status: :created, location: @file_info }
      else
        format.html { render action: "new" }
        format.json { render json: @file_info.errors, status: :unprocessable_entity }
      end
    end
  end

  # PUT /file_infos/1
  # PUT /file_infos/1.json
  def update
    @file_info = FileInfo.find(params[:id])

    respond_to do |format|
      if @file_info.update_attributes(params[:file_info])
        format.html { redirect_to @file_info, notice: 'File info was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: "edit" }
        format.json { render json: @file_info.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /file_infos/1
  # DELETE /file_infos/1.json
  def destroy
    @file_info = FileInfo.find(params[:id])
    @file_info.destroy

    respond_to do |format|
      format.html { redirect_to file_infos_url }
      format.json { head :no_content }
    end
  end
end
