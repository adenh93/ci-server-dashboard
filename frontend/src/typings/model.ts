export interface Build {
    slug: string;
    build_status: string;
    build_completed_time: Date;
    build_duration: number;
    build_artifacts: BuildArtifact[];
    commit_branch: string;
    commit_hash: string;
    commit_message: string;
    commit_author: string;
    commit_author_thumb_url: string;
}

export interface BuildArtifact {
    file_name: string;
    file_size: number;
}